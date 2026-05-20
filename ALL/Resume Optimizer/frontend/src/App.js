import React, { useState } from "react";
import axios from "axios";
import { Pie } from "react-chartjs-2";
import "chart.js/auto";
import "./App.css";

function App() {
  const [file, setFile] = useState(null);
  const [jobDesc, setJobDesc] = useState("");
  const [result, setResult] = useState(null);
  const [loading, setLoading] = useState(false);

  const handleSubmit = async (e) => {
    e.preventDefault();

    if (!file || !jobDesc) {
      alert("Please upload resume and enter job description");
      return;
    }

    setLoading(true);

    const formData = new FormData();
    formData.append("file", file);
    formData.append("job_desc", jobDesc);

    try {
      const res = await axios.post(
        "http://localhost:8000/analyze/",
        formData,
        {
          headers: {
            "Content-Type": "multipart/form-data",
          },
        }
      );

      console.log("Response:", res.data); // ✅ debug
      setResult(res.data.analysis);

    } catch (err) {
      console.error("FULL ERROR:", err); // 🔥 IMPORTANT
      alert("Check console (F12) for exact error");
    } finally {
      setLoading(false);
    }
  };

  const chartData = result && {
    labels: ["Matched", "Missing"],
    datasets: [
      {
        data: [
          result.matched_keywords.length,
          result.missing_keywords.length,
        ],
        backgroundColor: ["#4caf50", "#f44336"],
      },
    ],
  };

  return (
    <div className="container">
      <h1>🚀 AI Resume Analyzer</h1>
      <p>Optimize your resume for ATS and get hired faster</p>

      <form onSubmit={handleSubmit} className="card">
        <input
          type="file"
          onChange={(e) => setFile(e.target.files[0])}
        />

        <textarea
          placeholder="Paste Job Description..."
          value={jobDesc}
          onChange={(e) => setJobDesc(e.target.value)}
        />

        <button type="submit" disabled={loading}>
          {loading ? "Analyzing..." : "Analyze Resume"}
        </button>
      </form>

      {result && (
        <div className="result">
          
          {/* Score */}
          <div
            className="score"
            style={{
              color:
                result.score > 70
                  ? "#4caf50"
                  : result.score > 40
                  ? "#ff9800"
                  : "#f44336",
            }}
          >
            {result.score}%
          </div>

          {/* Progress Bar */}
          <div
            style={{
              width: "300px",
              height: "10px",
              background: "#ddd",
              margin: "10px auto",
              borderRadius: "5px",
            }}
          >
            <div
              style={{
                width: `${result.score}%`,
                height: "100%",
                background:
                  result.score > 70
                    ? "#4caf50"
                    : result.score > 40
                    ? "#ff9800"
                    : "#f44336",
                borderRadius: "5px",
              }}
            />
          </div>

          {/* Chart */}
          <div style={{ width: "300px", margin: "20px auto" }}>
            <Pie data={chartData} />
          </div>

          {/* Skills Section */}
          <div className="grid">
            <div className="box">
              <h3>✅ Matched</h3>
              <ul>
                {result.matched_keywords.map((item, i) => (
                  <li key={i}>{item}</li>
                ))}
              </ul>
            </div>

            <div className="box">
              <h3>❌ Missing</h3>
              <ul>
                {result.missing_keywords.map((item, i) => (
                  <li key={i}>{item}</li>
                ))}
              </ul>
            </div>
          </div>

        </div>
      )}
    </div>
  );
}

export default App;