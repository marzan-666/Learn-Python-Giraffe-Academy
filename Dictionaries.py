monthConversions = {
    "Jan" : "Januray",
    "Feb" : "Februaru",
    "Mar" : "March",
    "Apr" : "April",
    "May" : "May",
    "Jun" : "June",
    "Jul" : "July",
    "Aug" : "August",
    "Sep" : "September",
    "Oct" : "October",
    "Nov" : "November",
    "Dec" : "December"
}
print(monthConversions.get("Jan"))
print(monthConversions.get("Man", "Not a valid key"))
monthConversions = {
    0: "Januray",
    1: "Februaru",
    2: "March",
    3: "April",
    4: "May",
    5: "June",
    6: "July",
    7: "August",
    8: "September",
    9: "October",
    10: "November",
    11: "December"
}

print(monthConversions.get(11))
