"""This is a solution for the love username problem"""

def love_username() -> int:
    """Return the number of amazing contests"""
    _ = int(input())
    grades = list(map(int, input().split(" ")))
    min_grade = grades[0]
    max_grade = grades[0]
    count = 0
    for grd in grades[1:]:
        if grd > max_grade:
            count +=1
            max_grade = grd
        if grd < min_grade:
            count +=1
            min_grade = grd
    return count


if __name__ == "__main__":
    print(love_username())
