# # studentOne = {
# #     'name': 'Kimmy',
# #     'course': "CPE",
# #               "age": 19
# # }
# # studentOneName = 'Kimmy'
# # studentOneCourse = 'CPE'
# # StudentOneAge = 19
# #
# # studentTwo = {
# #     'name':'Gian',
# #     'course':'CPE',
# #     'age':18
# # }
# #
# #
# # # print(studentOne)
# # # print(studentTwo)
# # # print(len(studentOne))
# #
# # # print(studentOne.keys())
# # # print(studentOne.values())
# #
# # students = [studentOne, studentTwo]
# # print(students)
# # print(students[1].get('name'))
# #
# # d = {"a": 1, "b": 2}
# # print(d["a"])
#
# # d = {"x": 10, "y": 20}
# # print(d.get("z"))
#
# # d = {"a": 1, "b": 2}
# # d["a"] = 5
# # print(d)
# #
# # d = {"a": 1, "b": 2}
# # #
# # d = {"x": 1, "y": 2, "z": 5}
# # print(d.popitem())
# #
#
# #
# # d = {"a": 1, "b": 2}
# # d.update({"c": 3})
# # # print(d)
# # d = {1: "A", 2: "B", 3: "C"}
# # print(d.get(4, "Not found"))
# #
# # d = {"a": 1, "b": 2}
# # print(d.setdefault("c", 5))
# # print(d)
# #
# # d = {"x": 10, "y": 20}
# # d2 = d
# # d2["x"] = 100
# # # print(d["x"])
# #
# # d = {"a": 1, "b": 2, "c": 3}
# # for k, v in d.items():
# # print(k, end="")
# #
# # d = {"a": [1,2], "b": [3,4]}
# # d2 = d.copy()
# # d2["a"].append(5)
# # print(d["a"])
# #
# # d = dict.fromkeys(["a", "b", "c"], 0)
# # print(d)
# #
# # d = {"a": 1}
# # d["b"] += 5
# #
# # d = {"x": 1, "y": 2, "z": 3}
# # print(list(d.keys())[1])
# #
# # d = {"a": 1, "b": 2}
# # print("c" not in d)
#
# d = {"a": 10, "b": 20}
# print(max(d))
#
# d = {"a":1, "b":2}
# print(sum(d.values()))
#
# d = {}
# d[1] = "A"
# d[True] = "B"
# print(d)

# d = { "a": 1, "b": 2 }
# print({v: k for k, v in d.items()})
#
# d = {"a": 1, "b": 2, "c": 3}
# for k, v in d.items():
#    print(k, end="")

d = dict.fromkeys(["a", "b", "c"], 0)
print(d)