# fsync

The goal of this project is to better understand the various technologies and techniques used in a file synchronisation application.

Some areas that may be covered (this is still early days):

- How are files compared?
- How are large files compared?
- How are files compared efficiently?
- How are files kept in sync?
- How are files efficiently synced?

## File Identification

Files can be identified through scanning the entire contents of the file. However, this is inefficient.

Instead, to identify a file more efficiently, an executive summary of the file's binary data is created in the form of a hash.

Hashes are theoretically unique for all different input values.

This enables even large files to be concisely summarised and easily checked for differences.

Various hashing algorithms exist and the popular Git Distributed Version Control System (Git) uses the Secure Hashing Algorithm 256 (SHA256) to compare files and commits.