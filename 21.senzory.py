signal = "0"
cas = 3

for i in range(1,cas+1):
    zakodovanie = ""
    for bit in signal:
        if bit == "0":
            zakodovanie += "01"
        else:
            zakodovanie += "10"
        signal = zakodovanie
print(signal)


# # # import random

# # # def encode_signal(time):
# # #     signal = "0"
# # #     for _ in range(1, time + 1):
# # #         encoded = ""
# # #         for bit in signal:
# # #             if bit == "0":
# # #                 encoded += "01"
# # #             else:
# # #                 encoded += "10"
# # #         signal = encoded
# # #     return signal

# # # chosen_time = random.randint(1, 6) 
# # # encoded_signal = encode_signal(chosen_time)
# # # print(f"Binárna zakódovaná postupnosť signálu v čase {chosen_time} sekúnd: {encoded_signal}")

# # # signal = "0"

# # # cas = 3

# # # for _ in range(1, cas+1):
# # #     zakodovanie = ""
# # #     for x in signal:
# # #         if x == "0":
# # #             zakodovanie += "01"
# # #         else:
# # #             zakodovanie += "10"
# # #     signal = zakodovanie

# # # print(zakodovanie)
# import random 
# signal = "0"
# cas = random.randint(1,6)

# for i in range(1,cas+1):
#     zakodovanie = ""
#     for x in signal:
#         if x == "0":
#             zakodovanie += "01"
#         else:
#             zakodovanie += "10"
#         signal = zakodovanie
# print(zakodovanie)



















signal = "0"
cas = 3

for i in range(1,cas+1):
    zakodovanie = ""
    for bit in signal:
        if bit == "0":
            zakodovanie += "01"
        else:
            zakodovanie += "10"
        signal = zakodovanie
print(signal)