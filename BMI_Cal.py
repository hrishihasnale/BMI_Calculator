
import pandas as pd


def BMI_Report(data):
	
	result = list(map(lambda x: BMI_Calculation(x),data))	
	df = pd.DataFrame(result)
	return df


def BMI_Calculation(obj):
	
	user_height_meter = obj['HeightCm']*2 / 100.0;
	BMI_range = round(obj['WeightKg'] / user_height_meter,2)
	
	if BMI_range <= 18.4:
		res = {'Gender':obj['gender'],
			'HeightCm':obj['HeightCm'],'WeightKg':obj['WeightKg'],'BMI Category':'Underwight','BMI Range (kg/m2)':BMI_range,'Health risk':'Malnutrition risk'}

	elif BMI_range >= 18.4 and BMI_range <= 24.9:
		res = {'Gender':obj['gender'],
			'HeightCm':obj['HeightCm'],'WeightKg':obj['WeightKg'],'BMI Category':'Normal weight','BMI Range (kg/m2)':BMI_range,'Health risk':'Low risk'}
	
	elif BMI_range >= 25 and BMI_range <= 29.9:
		res = {'Gender':obj['gender'],
			'HeightCm':obj['HeightCm'],'WeightKg':obj['WeightKg'],'BMI Category':'Overweight','BMI Range (kg/m2)':BMI_range,'Health risk':'Enhanced risk'}

	elif BMI_range >= 30 and BMI_range <= 34.9:
		res = {'Gender':obj['gender'],
			'HeightCm':obj['HeightCm'],'WeightKg':obj['WeightKg'],'BMI Category':'Moderately obese','BMI Range (kg/m2)':BMI_range,'Health risk':'Medium risk'}

	elif BMI_range >= 35 and BMI_range <= 39.9:
		res = {'Gender':obj['gender'],
			'HeightCm':obj['HeightCm'],'WeightKg':obj['WeightKg'],'BMI Category':'Severely obese','BMI Range (kg/m2)':BMI_range,'Health risk':'High risk'}

	else:
		res = {'Gender':obj['gender'],
			'HeightCm':obj['HeightCm'],'WeightKg':obj['WeightKg'],'BMI Category':'Very severely obese','BMI Range (kg/m2)':BMI_range,'Health risk':'Very high risk'}
	
	return res 




# INPUT

input_data = [
			{"gender":"Male","HeightCm":171,"WeightKg":96},
			{"gender":"Male","HeightCm":161,"WeightKg":85},
			{"gender":"Male","HeightCm":180,"WeightKg":77},
			{"gender":"Female","HeightCm":166,"WeightKg":62},
			{"gender":"Female","HeightCm":150,"WeightKg":70},
			{"gender":"Female","HeightCm":167,"WeightKg":82}
			]

print(BMI_Report(input_data))