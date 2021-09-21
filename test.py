import pytest
import app
from app import check_document_existance, get_doc_owner_name, get_all_doc_owners_names
from app import remove_doc_from_shelf, add_new_shelf, append_doc_to_shelf
from app import delete_doc, get_doc_shelf, move_doc_to_shelf
from app import show_document_info, show_all_docs_info, add_new_doc



# documents = [
#     {"type": "passport", "number": "2207 876234", "name": "Василий Гупкин"},
#     {"type": "invoice", "number": "11-2", "name": "Геннадий Покемонов"},
#     {"type": "insurance", "number": "10006", "name": "Аристарх Павлов"}
# ]
#
# directories = {
#     '1': ['2207 876234', '11-2', '5455 028765'],
#     '2': ['10006'],
#     '3': []
# }


class TestDocuments:
    def setup(self):
        print('method setup')

    def teardown(self):
        print('method teardown')

    def test_check_document_existance(self):
        documents_check_list = ["2207 876234", "11-2", "10006"]
        for document in documents_check_list:
            assert check_document_existance(document) == True

    def test_check_not_document_existance(self):
        wrong_documents_check_list = ["125"]
        for document in wrong_documents_check_list:
            assert check_document_existance(document) == False

    def test_get_doc_owner_name(self):
        assert get_doc_owner_name("11-2") == "Геннадий Покемонов"

    def test_not_get_doc_owner_name(self):
        assert get_doc_owner_name("11-2") != "John Doe"

    def test_get_all_doc_owners_names(self):
        checked_user_list = ["Василий Гупкин", "Геннадий Покемонов", "Аристарх Павлов"]
        assert get_all_doc_owners_names() == set(checked_user_list)

    def test_not_get_all_doc_owners_names(self):
        checked_user_list = ["Илларион Чувайлов", "Григорий Распутин", "Аристарх Павлов"]
        assert get_all_doc_owners_names() != set(checked_user_list)

    def test_remove_doc_from_shelf(self):
        remove_doc_from_shelf("10006")
        assert "10006" not in app.directories

    def test_add_new_shelf(self):
        assert add_new_shelf("4") == ("4", True)

    def test_not_add_new_shelf(self):
        assert add_new_shelf("1") == ("1", False)

    def test_append_doc_to_shelf(self):
        append_doc_to_shelf("5006", "8")
        assert "5006" in app.directories["8"]

    def test_append_doc_to_existing_shelf(self):
        append_doc_to_shelf("58", "1")
        assert "58" in app.directories["1"]

    def test_delete_doc(self):
        delete_doc("11-2")
        assert "11-2" not in app.documents, app.directories
    # ???

    # def test_get_doc_shelf(self):
    #     assert get_doc_shelf("10006") == '2'

    def test_move_doc_to_shelf(self):
        assert move_doc_to_shelf("10006","3") == 'Документ номер "10006" был перемещен на полку номер "3"'

    def test_not_exist_move_doc_to_shelf(self):
        assert move_doc_to_shelf("855","3") == 'Документ номер "855" был перемещен на полку номер "3"'

# ???
#     def test_show_document_info(self):
#         assert show_document_info('11-2') == '"invoice" 11-2 "Геннадий Покемонов"'

