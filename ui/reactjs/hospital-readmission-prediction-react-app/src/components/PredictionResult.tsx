import type { PredictionResponse } from "../models/PredictionResponse";

interface Props {
    result: PredictionResponse;
}

export default function PredictionResult({ result }: Props) {

    const probability = Math.round(result.probability * 100);

    return (

        <div className="result-card">

            <h2>Prediction Result</h2>

            <div className="result-grid">

                <div className="result-box">

                    <div className="title">
                        Prediction
                    </div>

                    <div className="value success">

                        {result.prediction}

                    </div>

                </div>

                <div className="result-box">

                    <div className="title">

                        Probability

                    </div>

                    <div className="circle">

                        {probability}%

                    </div>

                </div>

                <div className="result-box">

                    <div className="title">

                        Risk Level

                    </div>

                    <div className={`risk ${result.risk_level.toLowerCase()}`}>

                        {result.risk_level}

                    </div>

                </div>

            </div>

        </div>

    );

}