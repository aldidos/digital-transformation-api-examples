import sys
sys.path.append('.')

from examples.base_uri import BaseAPI, headers, data_to_json
import requests

def create_workout(exercise_library, completed_sets, start_time, end_time) : 
    return {
        'exercise_library' : exercise_library, 
        'completed_sets' : completed_sets, 
        'start_time' : start_time, 
        'end_time' : end_time
    }

def create_workout_set(set, weight, total_reps, set_start_time, set_end_time, res_start_time, res_end_time) : 
    return {
        'set' : set, 
        'weight' : weight, 
        'total_reps' : total_reps, 
        'set_start_time' : set_start_time, 
        'set_end_time' : set_end_time, 
        'res_start_time' : res_start_time, 
        'res_end_time' : res_end_time
    }

def create_workout_metric(rep, peak_velocity_con, mean_velocity_con, peak_power_con, mean_power_con, 
                          peak_foce_con, mean_foce_con, peak_acceleration_con, mean_acceleration_con, 
                          peak_velocity_ecc, mean_velocity_ecc, peak_power_ecc, mean_power_ecc, peak_foce_ecc, mean_foce_ecc, 
                          peak_acceleration_ecc, mean_acceleration_ecc, rep_duration_con, rep_duration_ecc, top_stay_duration, 
                          bottom_stay_duration, rep_duration, RSI, RFD
                          ) : 
    return {
        'rep' : rep, 
        'peak_velocity_con' : peak_velocity_con, 
        'mean_velocity_con' : mean_velocity_con, 
        'peak_power_con' : peak_power_con,
        'mean_power_con' : mean_power_con, 
        'peak_foce_con' : peak_foce_con,
        'mean_foce_con' : mean_foce_con, 
        'peak_acceleration_con' : peak_acceleration_con,
        'mean_acceleration_con' : mean_acceleration_con, 
        'peak_velocity_ecc' : peak_velocity_ecc,
        'mean_velocity_ecc' : mean_velocity_ecc, 
        'peak_power_ecc' : peak_power_ecc,
        'mean_power_ecc' : mean_power_ecc, 
        'peak_foce_ecc' : peak_foce_ecc,
        'mean_foce_ecc' : mean_foce_ecc, 
        'peak_acceleration_ecc' : peak_acceleration_ecc,
        'mean_acceleration_ecc' : mean_acceleration_ecc, 
        'rep_duration_con' : rep_duration_con,
        'rep_duration_ecc' : rep_duration_ecc, 
        'top_stay_duration' : top_stay_duration,
        'bottom_stay_duration' : bottom_stay_duration, 
        'rep_duration' : rep_duration,
        'RSI' : RSI, 
        'RFD' : RFD,
    }

def create_dumydata() : 
    return {
        'workout' : create_workout(1, 2, '2025-02-11 15:30:00', '2025-02-11 15:45:00'),
        'workout_sets' : [
            {
                'workout_set' : create_workout_set(1, 70, 5, '2025-02-11 15:30:00', '2025-02-11 15:34:00', '2025-02-11 15:34:00', '2025-02-11 15:35:00'),
                'workout_metrics' : [
                    create_workout_metric(1, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.1, 0.1, 0.1, 0.1, 0.5, 0.9, 0.9),
                    create_workout_metric(2, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.1, 0.1, 0.1, 0.1, 0.5, 0.9, 0.9),
                    create_workout_metric(3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.1, 0.1, 0.1, 0.1, 0.5, 0.9, 0.9),
                    create_workout_metric(4, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.1, 0.1, 0.1, 0.1, 0.5, 0.9, 0.9),
                    create_workout_metric(5, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.1, 0.1, 0.1, 0.1, 0.5, 0.9, 0.9),
                ]
            },
            {
                'workout_set' : create_workout_set(2, 90, 5, '2025-02-11 15:36:00', '2025-02-11 15:42:00', None, None),
                'workout_metrics' : [
                    create_workout_metric(1, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.1, 0.1, 0.1, 0.1, 0.5, 0.9, 0.9),
                    create_workout_metric(2, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.1, 0.1, 0.1, 0.1, 0.5, 0.9, 0.9),
                    create_workout_metric(3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.1, 0.1, 0.1, 0.1, 0.5, 0.9, 0.9),
                    create_workout_metric(4, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.1, 0.1, 0.1, 0.1, 0.5, 0.9, 0.9),
                    create_workout_metric(5, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.1, 0.1, 0.1, 0.1, 0.5, 0.9, 0.9),
                ]
            }
        ]
    }


class WorkoutSessionWorkouts(BaseAPI) : 

    def __init__(self, uri) : 
        super().__init__(uri)

data = create_dumydata()

user_id = 1
workout_session_id = 1
if __name__ == '__main__' : 
    uri = f'/users/{user_id}/workout_sessions/{workout_session_id}/workouts' 
    api = WorkoutSessionWorkouts(uri)

    api.post(data)


  