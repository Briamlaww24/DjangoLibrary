from .authorViews import authorDetail, authorList
from .bookViews import bookDetail, bookList, bookPdf, bookRead, createBook, deleteBook, editBook
from .categoryViews import categoryCreate, categoryDelete, categoryDetail, categoryEdit, categoryList
from .loanViews import loanDetail, loanList

__all__ = [
    "authorDetail", "authorList",
    "bookDetail", "bookList", "bookPdf", "bookRead", "createBook", "deleteBook", "editBook",
    "categoryCreate", "categoryDelete", "categoryDetail", "categoryEdit", "categoryList",
    "loanDetail", "loanList",
]
