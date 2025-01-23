from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import (CharacterTextSplitter,
                                      RecursiveCharacterTextSplitter)

import os

q1_pdf = "OpenSourceLicenses.pdf"
q2_pdf = "勞動基準法.pdf"


def hw02_1(q1_pdf):
    pdf_path = os.getcwd() + os.sep + q1_pdf
    if os.path.isfile(pdf_path):
        pdf_loader = PyPDFLoader(pdf_path)
        documents = pdf_loader.load()
        text_splitter = CharacterTextSplitter(
            chunk_size=1000,
            chunk_overlap=0
        )
        split_documents = text_splitter.split_documents(documents)
        return split_documents[-1]
    else:
        print("Invalid file path")
        return

def hw02_2(q2_pdf):
    pass