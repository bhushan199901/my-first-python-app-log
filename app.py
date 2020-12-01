# main application - App.py
from CompanyBlog import app
import os

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8000))
    app.run(debug=True, port=port)
