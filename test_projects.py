from api_project import ProjectApi

class TestYougileProjects:

    def test_create_project_positive(self):
    #Позитивный тест на создание проекта
        response = ProjectApi.create_project("Test Project", "This is a test project")
        assert response.status_code == 201
        assert response.json().get("name") == "Test Project"

    def test_create_project_negative(self):
       #Негативный тест на создание проекта без имени
        response = ProjectApi.create_project("", "This is a test project without a name")
        assert response.status_code == 400  

    def test_update_project_positive(self):
        #Позитивный тест на обновление проекта
        project_id = 1  
        response = ProjectApi.update_project(project_id, "Updated Test Project")
        assert response.status_code == 200
        assert response.json().get("name") == "Updated Test Project"

    def test_update_project_negative(self):
        #Негативный тест на обновление несуществующего проекта
        project_id = 9999  
        response = ProjectApi.update_project(project_id, "Updated Test Project")
        assert response.status_code == 404  

    def test_get_project_positive(self):
    #Позитивный тест на получение проекта
        project_id = 1  
        response = ProjectApi.get_project(project_id)
        assert response.status_code == 200
        assert response.json().get("id") == project_id

    def test_get_project_negative(self):
        """Негативный тест на получение несуществующего проекта"""
        project_id = 9999  
        response = ProjectApi.get_project(project_id)
        assert response.status_code == 404
