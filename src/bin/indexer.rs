#[macro_use]
extern crate log;

use gallop::core::index::TantivyIndex;
use gallop::clients::packer::{LocalPackerClient, PackerClientWrapper};
use futures::Future;
use grpcio::{RpcContext, UnarySink};

use gallop::protos::common::Error;
use gallop::protos::common::{Segment, SegmentId};
use gallop::protos::packer::SegmentRequest;
use gallop::protos::packer_grpc::PackerClient;
use std::sync::Arc;

use grpcio::{ChannelBuilder, EnvBuilder};

use gallop::protos::indexer::{
    BindRequest, CountRequest, CountResponse, QueryRequest, QueryResponse, UnBindRequest,
};
use gallop::{
    core::grpc,
    core::index::IndexWrapper,
    protos::indexer_grpc::{self, Indexer},
};

#[cfg(test)]
use mockall::{automock, predicate::*};

#[derive(Clone)]
struct IndexerService {
    inner: InnerIndexerService<LocalPackerClient, TantivyIndex>,
}

impl IndexerService {
    fn new() -> Self {
        Self {
            inner: InnerIndexerService::new(),
        }
    }
}

impl Indexer for IndexerService {
    fn query(&mut self, _ctx: RpcContext, _req: QueryRequest, _sink: UnarySink<QueryResponse>) {
        unimplemented!();
    }

    fn count(&mut self, _ctx: RpcContext, _req: CountRequest, _sink: UnarySink<CountResponse>) {
        unimplemented!();
    }

    fn bind(&mut self, ctx: RpcContext, req: BindRequest, sink: UnarySink<Error>) {
        info!("Got request to bid segment...");
        let segment_id = req.get_segment_id();
        let _segment = self.inner.pull(segment_id.clone());
        let mut resp = Error::default();
        resp.set_code(0);
        resp.set_message("OK!".to_string());
        let f = sink
            .success(resp)
            .map_err(move |e| println!("failed to reply {:?}: {:?}", req, e))
            .map(|_| ());
        ctx.spawn(f)
    }
    fn un_bind(&mut self, ctx: RpcContext, req: UnBindRequest, sink: UnarySink<Error>) {
        let mut resp = Error::default();
        resp.set_code(0);
        resp.set_message("OK!".to_string());
        let f = sink
            .success(resp)
            .map_err(move |e| println!("failed to reply {:?}: {:?}", req, e))
            .map(|_| ());
        ctx.spawn(f)
    }
}
#[derive(Clone)]
struct InnerIndexerService<C: PackerClientWrapper, I: IndexWrapper> {
    packer_client_wrapper: C,
    index_wrapper: I,
}

impl<C: PackerClientWrapper, I: IndexWrapper> InnerIndexerService<C, I> {
    fn new() -> Self {
        Self {
            packer_client_wrapper: C::from_addr("localhost:8081".to_string()),
            index_wrapper: I::new(),
        }
    }

    #[allow(dead_code)]
    fn from(packer_client_wrapper: C) -> Self {
        let index_wrapper = I::new();
        Self { packer_client_wrapper, index_wrapper }
    }

    fn pull(&self, segment_id: SegmentId) -> Segment {
        let resp = self.packer_client_wrapper.segment(segment_id).unwrap();
        resp
    }
}

#[cfg(test)]
mod tests {
    use super::{InnerIndexerService, SegmentId};

}


fn main() {
    let service = IndexerService::new();
    grpc::serve(indexer_grpc::create_indexer(service), 8082);
}
