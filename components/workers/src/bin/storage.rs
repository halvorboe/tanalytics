use std::io::Read;
use std::sync::Arc;
use std::{io, thread};

use futures::sync::oneshot;
use futures::Future;
use grpcio::{Environment, RpcContext, ServerBuilder, UnarySink};

use gallop::protos::common::{Error, Row};
use gallop::protos::storage::SegmentId;
use gallop::protos::storage::{
    ConfigureRequest, InsertRequest, SegmentRequest, SegmentResponse, SegmentsRequest,
    SegmentsResponse,
};
use gallop::protos::storage_grpc::{self, Storage};

use gallop::core::codec;
use gallop::core::config::{Configuration};
use gallop::core::directory::{Directory, InMemoryDirectory};
use gallop::core::grpc;

use chrono::{DateTime, NaiveDateTime, Utc};

#[derive(Clone)]
struct StorageService {
    inner: InnerStorageService,
}

impl StorageService {
    fn new() -> Self {
        Self {
            inner: InnerStorageService::default(),
        }
    }
}

impl Storage for StorageService {
    
    fn insert(&mut self, ctx: RpcContext, req: InsertRequest, sink: UnarySink<Error>) {
        let table_name = req.get_table_name().to_string();
        let row = req.get_row();
        self.inner.insert(table_name, row.clone());
        let mut resp = Error::default();
        resp.set_code(0);
        resp.set_message("OK!".to_string());
        let f = sink
            .success(resp)
            .map_err(move |e| println!("failed to reply {:?}: {:?}", req, e))
            .map(|_| ());
        ctx.spawn(f)
    }
    fn segment(&mut self, ctx: RpcContext, req: SegmentRequest, sink: UnarySink<SegmentResponse>) {
        let segment_id = req.get_segment_id();
        let segment = self.inner.segment("124".to_string());
        let mut resp = SegmentResponse::default();


        let f = sink
            .success(resp)
            .map_err(move |e| println!("failed to reply {:?}: {:?}", req, e))
            .map(|_| ());
        ctx.spawn(f) 

    }
    fn segments(
        &mut self,
        ctx: RpcContext,
        req: SegmentsRequest,
        sink: UnarySink<SegmentsResponse>,
    ) {
        let segments = self.inner.segments();
        let mut resp = SegmentsResponse::default();
        let f = sink
            .success(resp)
            .map_err(move |e| println!("failed to reply {:?}: {:?}", req, e))
            .map(|_| ());
        ctx.spawn(f) 
    }
}

#[derive(Clone)]
struct InnerStorageService {
    config: Configuration,
    directory: InMemoryDirectory,
}

impl InnerStorageService {
    fn default() -> Self {
        Self {
            config: Configuration::default(),
            directory: InMemoryDirectory::new(),
        }
    }

    fn insert(&mut self, table_name: String, row: Row) {
        let mut segment_id = SegmentId::new();
        segment_id.set_table(table_name.clone());
        segment_id.set_resolution(self.config.segment_resolution);
        segment_id.set_timestamp(codec::row::encode_timestamp(row.get_timestamp() as u128, self.config.segment_resolution));
        self.directory.append(table_name, codec::row::encode(&row))
    }

    fn segments(&self) -> Vec<String> {
        self.directory.list()
    }

    fn segment(&self, name: String) -> Vec<Row> {
        self.directory
            .read(name)
            .iter()
            .map(|it| codec::row::decode(it))
            .collect()
    }
}

fn main() {
    let service = StorageService::new();
    grpc::serve(storage_grpc::create_storage(service));
}

mod tests {

    use super::InnerStorageService;
    use gallop::protos::common::Row;

    #[test]
    fn test_basic() {
        let mut row = Row::new();
        row.set_timestamp(10_000_000_000_000_000);
        row.set_data(String::from("{\"title\":\"Hello, world!\"}"));
        let mut service = InnerStorageService::default();
        service.insert(String::from("a"), row.clone());
        service.insert(String::from("b"), row.clone());
        assert!(service.segments().len() == 2);
    }

    #[test]
    fn test_file_content() {
        let mut row = Row::new();
        row.set_timestamp(10_000_000_000_000_000);
        row.set_data(String::from("{\"title\":\"Hello, world!\"}"));
        let mut service = InnerStorageService::default();
        service.insert(String::from("a"), row.clone());
        let segment = &service.segments()[0];
        let rows = service.segment(segment.to_string());
        assert_eq!(rows[0], row);
    }
}
