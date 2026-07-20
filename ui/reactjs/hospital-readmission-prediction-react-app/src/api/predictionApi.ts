import apiClient from './apiClient';
import type {PredictionRequest} from '../models/PredictionRequest';
import type {PredictionResponse} from '../models/PredictionResponse';
export const predict=(data:PredictionRequest)=>apiClient.post<PredictionResponse>('/predict/',data).then(r=>r.data);