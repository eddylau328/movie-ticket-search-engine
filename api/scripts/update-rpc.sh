# Path to this plugin
PROTOC_GEN_TS_PATH="./node_modules/.bin/protoc-gen-ts"

PROTOC_GEN_GRPC_PATH="./node_modules/.bin/grpc_tools_node_protoc_plugin"

# Directory to write generated code to (.js and .d.ts files)
OUT_DIR="./grpc"

protoc \
    --plugin="protoc-gen-ts=${PROTOC_GEN_TS_PATH}" \
    --plugin="protoc-gen-grpc=${PROTOC_GEN_GRPC_PATH}" \
    --ts_out="service=grpc-node:${OUT_DIR}" \
    --js_out="import_style=commonjs,binary:${OUT_DIR}" \
    --grpc_out="${OUT_DIR}" \
    -I ../ \
    control-plane.proto