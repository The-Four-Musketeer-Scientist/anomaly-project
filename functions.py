import pandas as pd


def print_top_lessons1(df):
    lessons = df[["program_id", "cohort_id", "path"]]
    program_1_lessons = lessons[lessons["program_id"] == 1]

    program_1_cohort_lesson_traffic = program_1_lessons.groupby(["cohort_id", "path"]).size().reset_index(name="traffic")
    lesson_traffic_total = program_1_cohort_lesson_traffic.groupby("path")["traffic"].sum().reset_index()

    top_lessons = lesson_traffic_total.nlargest(4, "traffic")

    print("Top 4 most visited lessons:")
    for index, lesson in top_lessons.iterrows():
        print("Lesson Path:", lesson["path"])
        print("Total Traffic:", lesson["traffic"])
        print("---------------------------")
        
def print_top_lessons2(df):
    lessons = df[["program_id", "cohort_id", "path"]]
    program_2_lessons = lessons[lessons["program_id"] == 2]

    program_2_cohort_lesson_traffic = program_2_lessons.groupby(["cohort_id", "path"]).size().reset_index(name="traffic")
    lesson_traffic_total = program_2_cohort_lesson_traffic.groupby("path")["traffic"].sum().reset_index()

    top_lessons = lesson_traffic_total.nlargest(4, "traffic")

    print("Top 4 most visited lessons:")
    for index, lesson in top_lessons.iterrows():
        print("Lesson Path:", lesson["path"])
        print("Total Traffic:", lesson["traffic"])
        print("---------------------------")
        
        
def print_top_lessons3(df):
    lessons = df[["program_id", "cohort_id", "path"]]
    program_3_lessons = lessons[lessons["program_id"] == 3]

    program_3_cohort_lesson_traffic = program_3_lessons.groupby(["cohort_id", "path"]).size().reset_index(name="traffic")
    lesson_traffic_total = program_3_cohort_lesson_traffic.groupby("path")["traffic"].sum().reset_index()

    top_lessons = lesson_traffic_total.nlargest(4, "traffic")

    print("Top 4 most visited lessons:")
    for index, lesson in top_lessons.iterrows():
        print("Lesson Path:", lesson["path"])
        print("Total Traffic:", lesson["traffic"])
        print("---------------------------")
        
def print_top_lessons4(df):
    lessons = df[["program_id", "cohort_id", "path"]]
    program_4_lessons = lessons[lessons["program_id"] == 4]

    program_4_cohort_lesson_traffic = program_4_lessons.groupby(["cohort_id", "path"]).size().reset_index(name="traffic")
    lesson_traffic_total = program_4_cohort_lesson_traffic.groupby("path")["traffic"].sum().reset_index()

    top_lessons = lesson_traffic_total.nlargest(4, "traffic")

    print("Top 4 most visited lessons:")
    for index, lesson in top_lessons.iterrows():
        print("Lesson Path:", lesson["path"])
        print("Total Traffic:", lesson["traffic"])
        print("---------------------------")


def process_lessons_data(lessons_df):
    df = lessons_df.groupby(["cohort_id", "path"]).size().reset_index(name="traffic")

    lesson_traffic_total = df.groupby("path")["traffic"].sum().reset_index()

    pattern = "^[^.]+/[^.]+$"

    lessons_with_traffic_equal_to_1 = lesson_traffic_total[
        (lesson_traffic_total["traffic"] == 1) &
        (lesson_traffic_total["path"].str.contains(".+/.+")) &
        (lesson_traffic_total["path"].str.match(pattern))
    ]
    
    return lessons_with_traffic_equal_to_1


