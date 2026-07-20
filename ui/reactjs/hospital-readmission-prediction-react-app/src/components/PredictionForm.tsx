import { useState } from "react";
import { predict } from "../api/predictionApi";
import type { PredictionRequest } from "../models/PredictionRequest";
import type { PredictionResponse } from "../models/PredictionResponse";
import PredictionResult from "./PredictionResult";
import "../styles/PredictionForm.css";

const initialState: PredictionRequest = {
    age: 71,
    diagnosis: "Diabetes",
    medications: 9,
    lab_result: 220,
    previous_admissions: 4,
    length_of_stay: 7,
    discharge_summary:
        "Patient discharged with unstable blood sugar and renal complications."
};

export default function PredictionForm() {

    const [form, setForm] = useState(initialState);

    const [loading, setLoading] = useState(false);

    const [result, setResult] = useState<PredictionResponse>();

    const updateField = (field: keyof PredictionRequest, value: any) => {

        setForm({
            ...form,
            [field]: value
        });

    };

    const onPredict = async () => {

        setLoading(true);

        try {

            const response = await predict(form);

            setResult(response);

        } finally {

            setLoading(false);

        }

    };

    return (

        <>

            <div className="prediction-card">

                <h2>Patient Information</h2>

                <div className="form-grid">

                    <div className="form-group">
                        <label>Age</label>
                        <input
                            type="number"
                            value={form.age}
                            onChange={(e) =>
                                updateField("age", Number(e.target.value))
                            }
                        />
                    </div>

                    <div className="form-group">
                        <label>Diagnosis</label>

                        <select
                            value={form.diagnosis}
                            onChange={(e) =>
                                updateField("diagnosis", e.target.value)
                            }
                        >
                            <option>Diabetes</option>
                            <option>Heart Failure</option>
                            <option>Hypertension</option>
                            <option>COPD</option>
                            <option>Kidney Disease</option>
                        </select>

                    </div>

                    <div className="form-group">
                        <label>Medications</label>
                        <input
                            type="number"
                            value={form.medications}
                            onChange={(e) =>
                                updateField("medications", Number(e.target.value))
                            }
                        />
                    </div>

                    <div className="form-group">
                        <label>Lab Result</label>
                        <input
                            type="number"
                            value={form.lab_result}
                            onChange={(e) =>
                                updateField("lab_result", Number(e.target.value))
                            }
                        />
                    </div>

                    <div className="form-group">
                        <label>Previous Admissions</label>
                        <input
                            type="number"
                            value={form.previous_admissions}
                            onChange={(e) =>
                                updateField(
                                    "previous_admissions",
                                    Number(e.target.value)
                                )
                            }
                        />
                    </div>

                    <div className="form-group">
                        <label>Length of Stay</label>
                        <input
                            type="number"
                            value={form.length_of_stay}
                            onChange={(e) =>
                                updateField(
                                    "length_of_stay",
                                    Number(e.target.value)
                                )
                            }
                        />
                    </div>

                    <div className="form-group full-width">

                        <label>Discharge Summary</label>

                        <textarea

                            rows={4}

                            value={form.discharge_summary}

                            onChange={(e) =>
                                updateField(
                                    "discharge_summary",
                                    e.target.value
                                )
                            }

                        />

                    </div>

                </div>

                <button

                    className="predict-btn"

                    onClick={onPredict}

                    disabled={loading}

                >

                    {loading ? "Predicting..." : "Predict Readmission"}

                </button>

            </div>

            {result && <PredictionResult result={result} />}

        </>

    );

}