from abc import ABC, abstractmethod


class Repository(ABC):
    @abstractmethod
    def add(self, obj):
        pass

    @abstractmethod
    def get(self, obj_id):
        pass

    @abstractmethod
    def get_all(self):
        pass

    @abstractmethod
    def update(self, obj_id, data):
        pass

    @abstractmethod
    def delete(self, obj_id):
        pass

    @abstractmethod
    def get_by_attribute(self, attr_name, attr_value):
        pass


class InMemoryRepository(Repository):
    _storage = {}  # Class variable to store data

    def __init__(self):
        self.repo_name = self.__class__.__name__
        if self.repo_name not in InMemoryRepository._storage:
            InMemoryRepository._storage[self.repo_name] = {}

    def add(self, obj):
        InMemoryRepository._storage[self.repo_name][obj.id] = obj

    def get(self, obj_id):
        return InMemoryRepository._storage[self.repo_name].get(obj_id)

    def get_all(self):
        return list(InMemoryRepository._storage[self.repo_name].values())

    def update(self, obj_id, data):
        obj = self.get(obj_id)
        if obj:
            obj.update(data)

    def delete(self, obj_id):
        if obj_id in InMemoryRepository._storage[self.repo_name]:
            del InMemoryRepository._storage[self.repo_name][obj_id]

    def get_by_attribute(self, attr_name, attr_value):
        return next((obj for obj in self.get_all() if getattr(obj, attr_name) == attr_value), None)