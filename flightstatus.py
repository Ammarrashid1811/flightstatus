import streamlit as st
import pandas as pd
import pickle

st.write("""
# Flight Status Prediction

This app predicts the **Flight status** 
""")

st.sidebar.header('User Input Parameters')

def user_input_features():
    CarrierCode = st.sidebar.selectbox('CarrierCode', [0, 1, 2, 3])
    FlightNumber = st.sidebar.selectbox('FlightNumber',[893, 512, 503, 723, 707, 890, 101, 354, 892, 856, 538, 346, 521, 384, 6225, 5121, 6441, 6308, 5213, 6320, 6307, 6449, 123, 375, 715, 713, 828, 888, 884, 5188, 5221, 6125, 1720, 5119, 6436, 6311, 6126, 393, 273, 6358, 6299, 5751, 5652, 1730, 6138, 6017, 12, 23, 68, 38, 348, 714, 353, 371, 712, 334, 513, 6322, 869, 5412, 6440, 6419, 6495, 6090, 6267, 5748, 5882, 502, 129, 540, 391, 5111, 1729, 5207, 5874, 1776, 6467, 6468, 5204, 6183, 1503, 5141, 53, 75, 13, 69, 822, 429, 271, 5194, 6314, 5749, 6226, 188, 6272, 5203, 1725, 6228, 5105, 5247, 5112, 1793, 72, 52, 10, 29, 716, 138, 420, 126, 704, 5202, 5645, 25, 889, 717, 404, 139, 584, 825, 6113, 5649, 6302, 73, 22, 46, 76, 826, 390, 524, 860, 418, 526, 582, 5740, 6317, 47, 545, 376, 6227, 5871, 6432, 6497, 141, 896, 6310, 9973, 6014, 6315, 5244, 5108, 6319, 186, 278, 534, 407, 886, 6203, 5304, 5651, 6016, 5104, 1490, 706, 270, 335, 5646, 6326, 5113, 6266, 374, 820, 829, 5303, 5233, 6112, 6128, 6122, 6354, 66, 28, 705, 883, 721, 703, 643, 6306, 6129, 525, 428, 187, 5870, 6433, 5228, 6182, 5116, 5173, 535, 6412, 6309, 5644, 6248, 5137, 5229, 5172, 377, 131, 897, 6355, 5210, 6321, 6418, 527, 5212, 5226, 887, 6462, 6262, 6263, 1791, 6496, 5138, 1792, 2139, 5140, 6071, 523, 130, 1234, 5209, 6064, 6051, 5220, 9228, 5109, 1774, 62, 381, 649, 118, 5195, 6052, 6034, 9013, 6465, 5419, 6059, 426, 1311, 5746, 6316, 6042, 6359, 6422, 5327, 6072, 6414, 6415, 1717, 45, 405, 330, 370, 5133, 5876, 6312, 385, 136, 189, 882, 718, 6439, 6015, 6075, 6431, 5206, 9441, 1724, 406, 128, 5242, 5597, 5883, 5752, 5302, 5013, 880, 423, 5875, 5118, 6438, 11, 395, 421, 5139, 733, 39, 6224, 6037, 6035, 6447, 6492, 44, 719, 386, 5743, 642, 79, 583, 821, 516, 5437, 6494, 5117, 6466, 5234, 6063, 5142, 590, 6304, 113, 585, 103, 143, 520, 857, 522, 5246, 5747, 824, 640, 6189, 1491, 6181, 827, 722, 6130, 63, 403, 528, 169, 116, 119, 1771, 591, 710, 5227, 5420, 5232, 5205, 5648, 157, 392, 6173, 819, 854, 117, 700, 6305, 431, 5197, 5245, 6242, 331, 402, 394, 517, 5107, 6249, 5198, 279, 379, 5110, 5134, 1581, 9213, 5106, 5647, 6076, 1560, 1522, 529, 648, 6040, 6410, 1726, 5418, 6423, 6144, 6091, 5877, 71, 537, 6353, 6187, 6260, 5744, 6469, 6243, 1794, 74, 380, 239, 6491, 1521, 823, 5193, 9645, 6131, 6092, 1575, 6043, 6499, 5436, 6460, 5199, 5346, 6246, 9876, 2138, 238, 5421, 5411, 6191, 1510, 6341, 539, 6229, 9723, 6446, 6273, 1758, 1511, 6264, 137, 6186, 6058, 6055, 6093, 5872, 272, 5136, 5211, 6247, 1583, 8561, 8002, 8032, 70, 122, 378, 5879, 78, 5878, 77, 182, 505, 798, 799, 519, 183, 288, 509, 218, 342, 170, 701, 289, 236, 504, 674, 665, 532, 303, 234, 677, 792, 307, 664, 237, 693, 533, 507, 221, 212, 638, 352, 355, 553, 634, 761, 610, 124, 3130, 3032, 3223, 3212, 321, 611, 645, 531, 3025, 3426, 3037, 3112, 3018, 3443, 3114, 181, 511, 322, 500, 3342, 3237, 3396, 3118, 3373, 3357, 3209, 4107, 3427, 4105, 4403, 3216, 764, 596, 3026, 3006, 3510, 3428, 552, 309, 658, 3254, 3159, 3440, 3521, 3332, 3310, 3246, 3015, 4113, 3016, 398, 253, 3437, 3028, 3230, 3565, 3555, 3161, 3554, 3553, 356, 255, 351, 4101, 3148, 3234, 3185, 411, 639, 907, 3029, 399, 3239, 3372, 3007, 3419, 3168, 3343, 3435, 254, 541, 3008, 3430, 3184, 765, 655, 614, 3210, 3109, 3208, 3091, 3436, 3009, 607, 243, 397, 3027, 3107, 3233, 175, 606, 573, 350, 3548, 3211, 176, 171, 760, 308, 3431, 3116, 3448, 3425, 357, 323, 569, 158, 121, 3439, 4111, 5503, 3241, 3108, 3445, 3017, 3030, 3238, 659, 1040, 3362, 3207, 530, 510, 637, 3511, 3309, 3215, 3331, 647, 3240, 3562, 3183, 3167, 8601, 3433, 3359, 3113, 4125, 3110, 3171, 3162, 3398, 568, 636, 597, 3075, 3564, 3260, 3115, 3568, 3501, 3245, 3170, 3031, 369, 1041, 251, 311, 3073, 657, 481, 3256, 3397, 3520, 3420, 3140, 3011, 3447, 396, 3119, 3102, 3231, 319, 3188, 3106, 1031, 3021, 3012, 3556, 3010, 312, 3522, 120, 3601, 3131, 3303, 153, 140, 358, 501, 588, 3258, 3438, 3182, 3374, 3356, 3232, 570, 3205, 3432, 3549, 851, 1030, 3429, 615, 776, 9802, 4123, 3543, 3235, 230, 146, 3218, 252, 786, 9042, 3005, 3259, 3092, 9304, 5501, 3558, 3308, 1043, 599, 1042, 3306, 3002, 646, 787, 656, 3201, 3217, 3250, 906, 324, 654, 3242, 618, 600, 144, 3117, 3224, 3358, 3434, 3024, 359, 737, 644, 736, 3022, 3103, 601, 9701, 814, 203, 557, 263, 205, 268, 555, 809, 180, 7519, 326, 626, 551, 8298, 7527, 7515, 226, 109, 805, 256, 8074, 641, 107, 462, 602, 210, 240, 262, 194, 265, 274, 812, 753, 7624, 7512, 155, 154, 554, 725, 550, 209, 7514, 7523, 269, 387, 201, 8454, 264, 267, 861, 193, 211, 506, 559, 536, 266, 544, 724, 463, 7518, 206, 200, 241, 8455, 508, 670, 108, 125, 7532, 191, 275, 257, 624, 627, 7526, 7511, 475, 808, 7625, 7510, 7513, 7520, 7522, 106, 127, 625, 7521, 773, 772, 227, 430, 223, 132, 287, 778, 1264, 782, 698, 777, 759, 314, 1265, 18, 921, 697, 616, 781, 783, 605, 93, 133, 190, 213, 604, 332, 771, 762, 225, 711, 885, 327, 310, 427, 8782, 8434, 603, 622, 8552, 219, 608, 621, 689, 217, 8768, 228, 651, 329, 343, 9181, 315, 320, 9048, 7149, 774, 613, 763, 313, 328, 612, 316, 231, 690, 8528, 92, 768, 767, 222, 6434, 6303, 6437, 6139, 9242, 6077, 732, 6269, 5114, 5508, 5219, 6020, 5345, 9, 24, 9986, 5741, 6450, 142, 5192, 5120, 5012, 5745, 6180, 818, 5873, 6448, 1773, 9191, 6464, 6461, 868, 419, 1502, 1580, 6192, 422, 6490, 5208, 9722, 5236, 720, 9302, 6038, 6313, 6324, 1235, 6145, 6430, 9700, 6118, 5326, 6323, 6424, 6329, 1310, 5131, 9190, 1772, 6172, 5196, 6083, 6124, 204, 1520, 1535, 6265, 1395, 1394, 5030, 5413, 6143, 5417, 1722, 5742, 67, 1757, 6116, 6078, 5216, 1727, 6193, 5035, 1516, 6451, 5301, 1410, 5432, 6352, 6190, 6185, 6435, 6054, 8011, 8001, 8008, 8033, 8018, 2402, 372, 373, 556, 5500, 9119, 3014, 562, 3900, 3394, 3375, 871])
    DepartureStation = st.sidebar.selectbox('DepartureStation', [26, 56, 85, 14, 89, 99, 5, 46, 48, 60, 96, 27, 76, 90, 9, 69, 1, 64, 38, 19, 32, 47, 44, 88, 103, 87, 66, 79, 45, 8, 6, 7, 75, 35, 36, 101, 17, 23, 54, 94, 105, 24, 65, 59, 80, 109, 11, 41, 67, 10, 18, 71, 12, 57, 34, 100, 39, 82, 25, 43, 95, 0, 77, 83, 50, 16, 84, 106, 104, 107, 4, 102, 86, 72, 74, 55, 21, 13, 33, 52, 91, 78, 22, 108, 63, 70, 61, 31, 42, 30, 73, 93, 51, 28, 3, 58, 62, 92, 97, 81, 98, 15, 40, 20, 29, 53, 49, 2, 68, 37])
    Arrivalstation = st.sidebar.selectbox('Arrivalstation', [60, 34, 99, 28, 57, 22, 86, 124, 17, 63, 39, 97, 81, 49, 58, 7, 44, 115, 113, 118, 51, 47, 96, 92, 95, 9, 68, 41, 109, 70, 71, 38, 105, 84, 72, 98, 50, 54, 21, 89, 29, 2, 11, 12, 74, 48, 62, 13, 80, 10, 23, 26, 25, 15, 14, 85, 122, 111, 27, 104, 69, 8, 0, 82, 42, 46, 40, 53, 90, 91, 33, 75, 24, 35, 59, 119, 16, 100, 20, 55, 83, 76, 19, 116, 78, 65, 114, 45, 121, 120, 93, 36, 6, 117, 123, 67, 64, 1, 32, 87, 110, 102, 61, 66, 101, 30, 5, 73, 88, 107, 52, 18, 4, 77, 56, 106, 31, 125, 94, 43, 112, 103, 3, 79, 108, 37])
    PAX = st.sidebar.selectbox('PAX', range(1,180))
    AOCHolder = st.sidebar.selectbox('AOCHolder', range(0,7))
    DelayCode = st.sidebar.selectbox('DelayCode', [32, 89, 93, 81, 86, 63, 18, 36, 41, 15, 62, 16, 20, 87, 5, 78, 21, 8, 94, 19, 47, 83, 46, 72, 66, 99, 14, 34, 3, 70, 71, 37, 51, 88, 77, 33, 6, 91, 48, 4, 43, 40, 65, 82, 61, 64, 35, 85, 2, 7, 42, 38, 52, 49, 1, 31, 84, 11, 44, 13])
    DelayTime = st.sidebar.number_input('DelayTime', value=0)
    data = {'CarrierCode': CarrierCode,
            'FlightNumber': FlightNumber,
            'DepartureStation': DepartureStation,
            'Arrivalstation': Arrivalstation,
            'PAX': PAX,
            'AOCHolder': AOCHolder,
            'DelayCode': DelayCode,
            'DelayTime': DelayTime}
    features = pd.DataFrame(data, index=[0])
    return features

df = user_input_features()

st.subheader('User Input parameters')
st.write(df)

loaded_model = pickle.load(open("flightdatac.h5", "rb"))

prediction = loaded_model.predict(df)

st.subheader('Prediction')
st.write(prediction)
