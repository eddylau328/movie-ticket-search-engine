import { EnquiryBotClient } from "../grpc/control-plane_grpc_pb";
import { credentials, Metadata, ServiceError } from "grpc";

const address = "localhost:2000";
const client = new EnquiryBotClient(address, credentials.createInsecure());

export { client };
