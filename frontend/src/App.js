import React, { useState } from "react";
import axios from "axios";
import "./App.css";

function App() {
  const [productName, setProductName] = useState("");
  const [description, setDescription] = useState("");
  const [productImage, setProductImage] = useState("");

  const [job, setJob] = useState(null);
  const [loading, setLoading] = useState(false);

  const generateImage = async () => {
    if (!productName || !description || !productImage) {
      alert("Please fill all fields");
      return;
    }

    setLoading(true);

    try {
      const response = await axios.post(
        "http://127.0.0.1:8000/jobs",
        {
          product_name: productName,
          description: description,
          product_image: productImage,
        }
      );

      setJob(response.data);
    } catch (error) {
      console.error(error);
      alert("Error connecting to backend");
    }

    setLoading(false);
  };

  return (
    <div className="container">
      <h1>GlitrAI Mini Content Engine</h1>

      <input
        type="text"
        placeholder="Product Name"
        value={productName}
        onChange={(e) => setProductName(e.target.value)}
      />

      <textarea
        placeholder="Description"
        value={description}
        onChange={(e) => setDescription(e.target.value)}
      />

      <input
        type="text"
        placeholder="Product Image URL"
        value={productImage}
        onChange={(e) => setProductImage(e.target.value)}
      />

      <button onClick={generateImage}>
        {loading ? "Generating..." : "Generate"}
      </button>

      {job && (
        <div className="result">
          <h2>Job Result</h2>

          <p>
            <strong>ID:</strong> {job.id}
          </p>

          <p>
            <strong>Status:</strong> {job.status}
          </p>

          <p>
            <strong>Product:</strong> {job.product_name}
          </p>

          {job.image_url && (
            <img
              src={job.image_url}
              alt="Generated"
            />
          )}
        </div>
      )}
    </div>
  );
}

export default App;