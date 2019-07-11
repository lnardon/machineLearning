import numpy as np
from sklearn.linear_model import LinearRegression

# Params to be analyzed
x = np.array([318.959991,316.709991,318.869995,310.100006,322.690002,323.850006,320.230011,313.579987,303.200012,297.429993,308.739990,306.649994,297.179993,290.170013,298.140015,300.839996,349.540009,348.170013,341.989990,379.570007,370.339996,352.450012,355.489990,356.410004,347.640015,338.690002,335.450012,305.500000,308.440002,321.899994,321.640015,320.100006,322.820007,319.269989,311.859985,305.010010,303.149994,301.660004,288.950012,280.739990,280.950012,263.239990,285.500000,279.440002,290.540009,289.459991,295.200012,294.839996,284.959991,299.019989,298.329987,299.100006,299.679993,300.989990,309.579987,307.519989,264.769989,310.700012,301.019989,294.799988,281.829987,261.950012,250.559998,262.799988,256.880005,252.229996,258.779999,259.589996,276.589996,271.779999,263.910004,260.000000,260.950012,294.140015,288.500000,314.859985,330.899994,334.850006,329.899994,337.320007,344.279999,346.410004,341.399994,341.059998,348.160004,351.399994,350.510010,331.279999,338.730011,344.000000,348.440002,354.309998,353.470001,347.489990,338.190002,325.829987,346.000000,347.869995,343.920013]).reshape((-1, 1))
# Known Rsults
y = np.array([315.799988,321.429993,315.579987,311.709991,308.809998,325.000000,316.329987,321.230011,301.839996,304.420013,296.739990,304.850006,307.250000,295.899994,292.250000,297.989990,328.440002,347.809998,345.459991,343.839996,369.089996,365.549988,354.000000,361.130005,358.450012,341.910004,339.910004,323.500000,291.700012,310.609985,320.869995,319.140015,320.700012,318.000000,318.410004,310.269989,302.260010,302.000000,296.940002,285.049988,284.799988,260.100006,273.260010,279.470001,281.440002,288.019989,288.760010,290.040009,296.690002,280.510010,303.559998,297.700012,298.480011,300.000000,301.910004,312.899994,270.260010,305.769989,313.950012,303.329987,293.950012,274.649994,264.519989,255.250000,264.609985,257.529999,261.000000,259.059998,265.700012,282.399994,269.290009,267.390015,260.679993,263.869995,301.049988,317.220001,308.250000,337.470001,328.390015,332.540009,338.260010,343.739990,340.500000,339.070007,343.339996,348.500000,349.000000,348.369995,333.160004,342.700012,342.329987,345.190002,356.339996,341.750000,352.000000,334.350006,325.000000,345.989990,340.049988])

# Creation and Training of the model
model =  LinearRegression()
model.fit(x,y)
linear_result = model.score(x,y)

# Prediction Based on Training data

nx = np.array(307.880005).reshape((-1, 1)) # Can be a single number or an array

y_pred = model.predict(nx)
print('Predicted response:', y_pred)
print( 'Accuracy:', linear_result )