# PDF RAG Assistant - Technical Documentation

## Overview
A Retrieval-Augmented Generation (RAG) system built with LangChain that enables semantic search and question-answering over PDF documents using local embeddings and FAISS vector storage.

## Core Architecture

### 1. Document Processing Pipeline
- **PDF Parsing**: Extracts text content from PDF files using PyPDF2
- **Text Chunking**: Implements recursive character splitting with overlap to maintain context
- **Embedding Generation**: Converts text chunks to vector representations using local embedding models
- **Vector Indexing**: Stores embeddings in FAISS for efficient similarity search

### 2. RAG Implementation
- **Retriever**: FAISS-based similarity search with configurable k-nearest neighbors
- **Context Augmentation**: Combines retrieved chunks with the user query
- **Response Generation**: Uses LLM to synthesize answers from retrieved context

### 3. Local Processing Stack
- **Embedding Model**: Locally hosted embedding generation for data privacy
- **Vector Store**: FAISS index stored on disk for persistent storage
- **Document Cache**: Processed documents stored for quick reloading

## Key Components

### src/ingest.py
Handles PDF loading, text extraction, and document chunking. Uses LangChain's document loaders and text splitters with configurable chunk size and overlap.

### src/embed_and_index.py
Manages embedding generation and FAISS index creation. Creates vector representations of document chunks and builds searchable indices.

### src/rag_app.py
Core RAG logic including query processing, retrieval, and response generation. Implements the complete question-answering pipeline.

### app.py
Streamlit interface for document upload, query input, and result display. Provides a user-friendly web interface for interacting with the RAG system.

## Technical Details

### Embedding Strategy
- Uses sentence-transformers compatible models
- Embeddings are generated locally without external API calls
- Supports configurable embedding dimensions

### Retrieval Mechanism
- Cosine similarity for vector matching
- Configurable top-k retrieval
- Score threshold filtering for relevance

### Context Management
- Dynamic context window based on query complexity
- Chunk overlap to preserve semantic boundaries
- Source attribution for retrieved content

## Configuration Options

### Environment Variables
- `EMBEDDING_MODEL`: Local embedding model name
- `CHUNK_SIZE`: Text chunk size in characters
- `CHUNK_OVERLAP`: Overlap between chunks
- `K_RETRIEVAL`: Number of chunks to retrieve

### Model Settings
- Embedding dimensions: 384-768 based on model
- Context window: Variable based on LLM capacity
- Temperature: Configurable for response creativity

## Performance Considerations

### Indexing
- Batch processing for large document sets
- Persistent storage to avoid re-indexing
- Memory-efficient chunking

### Search
- FAISS optimized for approximate nearest neighbor
- GPU acceleration support if available
- Query caching for repeated questions

### Response Generation
- Context truncation for long responses
- Streaming support for real-time answers
- Token limit management

## Extensibility Points

### 1. Document Formats
Can be extended to support DOCX, TXT, HTML, and other formats through additional document loaders.

### 2. Embedding Models
Modular design allows swapping embedding models without changing the core pipeline.

### 3. Vector Stores
While currently using FAISS, can be extended to support Pinecone, Weaviate, or Chroma.

### 4. LLM Integration
Designed to work with various LLM backends through LangChain's LLM abstraction.

## Development Status

This is an ongoing project focusing on:
- Improving retrieval accuracy through better chunking strategies
- Enhancing context relevance scoring
- Adding multi-modal support (images, tables in PDFs)
- Implementing hybrid search (semantic + keyword)
- Adding conversation history and follow-up questions

## Future Roadmap

### Short-term
- [ ] Advanced chunking strategies (semantic, recursive)
- [ ] Query expansion and rephrasing
- [ ] Response citation and source highlighting

### Medium-term
- [ ] Multi-document summarization
- [ ] Cross-document relationship mapping
- [ ] Automated document categorization

### Long-term
- [ ] Real-time document updates
- [ ] Collaborative filtering for query improvement
- [ ] Advanced analytics on document usage patterns

## Integration Points
- Can be deployed as a standalone service
- API endpoints for programmatic access
- Webhook support for document processing events
- Export functionality for processed data

This project represents a scalable, privacy-focused approach to document intelligence that can be deployed in various environments from local machines to enterprise servers.