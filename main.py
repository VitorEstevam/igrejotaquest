from connections.designerDAO import DesignerDAO


# designer
d = DesignerDAO()
resp = d.update_on_db(67, 'vitor braga')

# id = d.insert_on_db("luana <3")
# resp = d.select_from_db(id)
# print(resp)
# all = d.select_all_from_db()
# print(all)

# print(d.update_on_db(id, 'luana show'))
# print(d.remove_from_db(id))
