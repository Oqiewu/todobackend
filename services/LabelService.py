from entity import Label
from repository import LabelRepository

class LabelService():
    def __init__(self, label_repository: LabelRepository.LabelRepository):
        self.label_repository = label_repository


    def add_label(self, Label: Label.Label):
        self.label_repository.add_label(Label)
    
    def delete_label(self, id: int):
        return self.label_repository.delete_label(id)
    
    def get_labels_list(self):
        return self.label_repository.get_labels_list()