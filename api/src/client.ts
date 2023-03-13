import { ControlPlaneClient } from "../grpc/control-plane_grpc_pb";
import { credentials, Metadata, ServiceError } from "@grpc/grpc-js";

const address = "localhost:50051";
const client = new ControlPlaneClient(address, credentials.createInsecure());
client.waitForReady(Date.now() + 5000, (error: Error | null) => {
  if (error) {
    console.error(error);
  } else {
    console.log("Client connected to server");
  }
});

export { client };
