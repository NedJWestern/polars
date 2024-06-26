use super::*;

#[cfg(feature = "ipc")]
mod ipc_file;

#[cfg(feature = "ipc_streaming")]
mod ipc_stream;
mod mmap;
#[cfg(any(feature = "ipc", feature = "ipc_streaming"))]
mod write;
#[cfg(all(feature = "async", feature = "ipc"))]
mod write_async;

#[cfg(feature = "ipc")]
pub use ipc_file::{IpcReader, IpcScanOptions};
#[cfg(feature = "ipc_streaming")]
pub use ipc_stream::*;
pub use write::{BatchedWriter, IpcCompression, IpcWriter, IpcWriterOption, IpcWriterOptions};

#[cfg(feature = "cloud")]
mod ipc_reader_async;
#[cfg(feature = "cloud")]
pub use ipc_reader_async::*;
