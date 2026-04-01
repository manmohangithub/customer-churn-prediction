import React, { useState, useEffect } from 'react'
import axios from 'axios'

export default function App(){

  const [form, setForm] = useState({
    TenureMonths: 5,
    MonthlyCharges: 70,
    TotalCharges: 350,
    Contract: "Month-to-month",
    InternetService: "DSL",
    PaymentMethod: "Electronic check",
    OnlineSecurity: "No",
    TechSupport: "No"
  })

  const [result, setResult] = useState(null)
  const [importance, setImportance] = useState({})

  const API = "http://127.0.0.1:8000"

  const handleChange = (e)=>{
    let value = e.target.value

    if (["TenureMonths","MonthlyCharges","TotalCharges"].includes(e.target.name)) {
      value = Number(value)
    }

    setForm({...form, [e.target.name]: value})
  }

  const predict = async ()=>{
    try {
      const payload = {
        TenureMonths: Number(form.TenureMonths),
        MonthlyCharges: Number(form.MonthlyCharges),
        TotalCharges: Number(form.TotalCharges),
        Contract: form.Contract,
        InternetService: form.InternetService,
        PaymentMethod: form.PaymentMethod,
        OnlineSecurity: form.OnlineSecurity,
        TechSupport: form.TechSupport
      }

      console.log("Sending:", payload)

      const res = await axios.post(API+"/predict", payload)
      setResult(res.data)

    } catch (err) {
      console.error(err.response?.data || err.message)
      alert(JSON.stringify(err.response?.data))
    }
  }

  const loadImportance = async ()=>{
    const res = await axios.get(API+"/feature-importance")
    setImportance(res.data)
  }

  useEffect(()=>{
    loadImportance()
  },[])

  return (
    <div style={{padding:20}}>
      <h2>🔥 Churn Prediction Dashboard</h2>

      <input type="number" name="TenureMonths" value={form.TenureMonths} onChange={handleChange} placeholder="Tenure (Months)" /><br/>

      <input type="number" name="MonthlyCharges" value={form.MonthlyCharges} onChange={handleChange} placeholder="Monthly Charges" /><br/>

      <input type="number" name="TotalCharges" value={form.TotalCharges} onChange={handleChange} placeholder="Total Charges" /><br/>

      <select name="Contract" onChange={handleChange}>
        <option>Month-to-month</option>
        <option>One year</option>
        <option>Two year</option>
      </select><br/>

      <select name="InternetService" onChange={handleChange}>
        <option>DSL</option>
        <option>Fiber optic</option>
        <option>No</option>
      </select><br/>

      <select name="PaymentMethod" onChange={handleChange}>
        <option>Electronic check</option>
        <option>Mailed check</option>
        <option>Bank transfer (automatic)</option>
        <option>Credit card (automatic)</option>
      </select><br/>

      <select name="OnlineSecurity" onChange={handleChange}>
        <option>No</option>
        <option>Yes</option>
        <option>No internet service</option>
      </select><br/>

      <select name="TechSupport" onChange={handleChange}>
        <option>No</option>
        <option>Yes</option>
        <option>No internet service</option>
      </select><br/><br/>

      <button onClick={predict}>🚀 Predict</button>

      {result && (
        <div>
          <h3>Churn: {result.churn}</h3>
          <h3>Probability: {result.probability.toFixed(2)}</h3>
        </div>
      )}

      <h3>📊 Feature Importance</h3>
      <ul>
        {Object.entries(importance).map(([k,v])=>(
          <li key={k}>{k}: {v.toFixed(3)}</li>
        ))}
      </ul>
    </div>
  )
}