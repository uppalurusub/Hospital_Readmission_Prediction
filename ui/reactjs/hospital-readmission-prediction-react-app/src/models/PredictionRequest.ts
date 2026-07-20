export interface PredictionRequest {
  age: number;
  diagnosis: string;
  medications: number;
  lab_result: number;
  previous_admissions: number;
  length_of_stay: number;
  discharge_summary: string;
}