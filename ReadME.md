# Stack
1. Back-end: streamlit with **pypdf loader**, langchain, Groq, HF embedding, chroma DB
2. Front end: css, html, js 

# Create these file/folder step by step
1. requirements.txt
2. data folder (place your pdf files in it)
3. vector_db_dir(it should be empty, files will create automatically when coe runs)
4. .env
5. main.py
6. vd.py

# Folder Structure
main_folder/
├── data/
│   └── ...                # Add your data files here (e.g., CSV, PDF, etc.)
├── vector_db_dir/
│   ├── 5fda9825-8220-4200-86be-51f973f4affa/
│   │   └── link_lists.bin # Example binary or vector files
│   └── chroma.sqlite3     # Database or other vector storage files
├── main.py                # Main application script
├── vd.py                  # Additional script (e.g., for vector database handling)
├── .env                   # Environment variables file (e.g., API keys, secrets)
└── requirements.txt       # Python dependencies

