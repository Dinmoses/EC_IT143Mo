import sqlite3

USERS = [
    # username, year, auth
    ("George_Washington", 1799, 1),
    ("John_Adams", 1826, 1),
    ("Thomas_Jefferson", 1826, 1),
    ("James_Madison", 1836, 1),
    ("James_Monroe", 1831, 1),
    ("John_Quincy_Adams", 1848, 1),
    ("Andrew_Jackson", 1845, 1),
    ("Martin_Van_Buren", 1862, 1),
    ("William_Henry_Harrison", 1841, 1),
    ("John_Tyler", 1862, 1),
    ("James_K_Polk", 1849, 1),
    ("Zachary_Taylor", 1850, 1),
    ("Millard_Fillmore", 1874, 1),
    ("Franklin_Pierce", 1869, 1),
    ("James_Buchanan", 1868, 1),
    ("Abraham_Lincoln", 1865, 1),
    ("Andrew_Johnson", 1875, 1),
    ("Ulysses_S_Grant", 1885, 1),
    ("Rutherford_B_Hayes", 1893, 1),
    ("James_A_Garfield", 1881, 1),
    ("Chester_A_Arthur", 1886, 1),
    ("Grover_Cleveland", 1908, 1),
    ("Benjamin_Harrison", 1901, 1),
    ("William_McKinley", 1901, 1),
    ("Theodore_Roosevelt", 1919, 1),
    ("William_H_Taft", 1930, 1),
    ("Woodrow_Wilson", 1924, 1),
    ("Warren_G_Harding", 1923, 1),
    ("Calvin_Coolidge", 1933, 1),
    ("Herbert_Hoover", 1964, 1),
    ("Franklin_D_Roosevelt", 1945, 1),
    ("Harry_S_Truman", 1972, 1),
    ("Dwight_D_Eisenhower", 1969, 1),
    ("John_F_Kennedy", 1963, 1),
    ("Lyndon_B_Johnson", 1973, 1),
    ("Richard_Nixon", 1994, 1),
    ("Gerald_Ford", 2006, 1),
    ("Jimmy_Carter", 2024, 1),  # update as needed
    ("Ronald_Reagan", 2004, 1),
    ("George_H_W_Bush", 2018, 1),
    ("Bill_Clinton", 9999, 1),
    ("George_W_Bush", 9999, 1),
    ("Barack_Obama", 9999, 1),
    ("Donald_Trump", 9999, 1),
    ("Joe_Biden", 9999, 1),
]

def insert_records():
    conn = sqlite3.connect('people.db')
    cursor = conn.cursor()

    cursor.executemany(
        "INSERT INTO users (username, year, auth) VALUES (?, ?, ?)",
        USERS
    )

    conn.commit()
    conn.close()
    print(f"Inserted {len(USERS)} user records into 'users'.")

if __name__ == "__main__":
    insert_records()
