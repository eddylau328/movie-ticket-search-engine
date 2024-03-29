import { ControlPlaneClient } from "../grpc/control-plane_grpc_pb";
import { credentials, Metadata, ServiceError } from "@grpc/grpc-js";

const address = process.env.CONTROL_PLANE_ADDRESS ?? "localhost:50051";
const client = new ControlPlaneClient(address, credentials.createInsecure());
client.waitForReady(Date.now() + 5000, (error?: Error) => {
  if (error) {
    console.error(error);
  } else {
    console.log("Client connected to server");
  }
});

export { client };
