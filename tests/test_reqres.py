from pages.get_page import Get_page
from pages.post_page import Post_page



def test_get_users1():
    gp = Get_page()
    gp.get_users_page2()
    pp = Post_page()
    pp.post_user({"name": "Morpheus", "job": "leader"})




