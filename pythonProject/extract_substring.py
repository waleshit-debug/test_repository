path = "89234567890	"
if "+7" in path:
    new_path = (
        path[:2]
        + " ("
        + path[2:5]
        + ") "
        + path[5:8]
        + "-"
        + path[8:10]
        + "-"
        + path[10:]
    )
else:
    new_path = (
        "+7" + " (" + path[1:4] + ") " + path[4:7] + "-" + path[7:9] + "-" + path[9:]
    )
print(new_path)
