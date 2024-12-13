import db
# 创建数据库
db = db.Database()

# 创建一个名为students的表，有三列：id、name、subject
columns = ["id", "name", "subject"]
db.create_table("students", columns)

# 插入数据
data = [(1, "Chen", "Math"), (2, "Liu", "Math"), (3, "Jiang", "Physics")]
for record in data:
    db.tables["students"].insert(record)

# 创建基于name列的平衡二叉树索引
db.tables["students"].create_index("name_index", "balanced_binary_tree", "name")

# 查询名字为Chen的学生信息
condition = {"name": "Chen"}
result = db.tables["students"].select(columns, condition)
print(result)

# 更新专业为物理的学生的名字为Wei
update_values = {"name": "Wei"}
db.tables["students"].update({"subject": "Physics"}, update_values)

# 删除3号学生记录
db.tables["students"].delete({"id": 3})