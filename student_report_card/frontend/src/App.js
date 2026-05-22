import './App.css';
import { useState } from 'react';

function App() {

  const [student, setStudent] = useState({
    id: '',
    name: '',
    maths: '',
    science: '',
    english: ''
  });

  const handleChange = (e) => {
    setStudent({
      ...student,
      [e.target.name]: e.target.value
    });
  };

  const handleSubmit = async () => {

    const response = await fetch("http://127.0.0.1:8000/student", {
      method: "POST",
      headers: {
        "Content-Type": "application/json"
      },
      body: JSON.stringify({
        id: Number(student.id),
        name: student.name,
        maths: Number(student.maths),
        science: Number(student.science),
        english: Number(student.english)
      })
    });

    const data = await response.json();

    alert(data.message);
  };

  return (
    <div className="App">

      <h1>Student Report Card</h1>

      <input
        type="number"
        name="id"
        placeholder="Student ID"
        onChange={handleChange}
      />

      <input
        type="text"
        name="name"
        placeholder="Student Name"
        onChange={handleChange}
      />

      <input
        type="number"
        name="maths"
        placeholder="Maths Marks"
        onChange={handleChange}
      />

      <input
        type="number"
        name="science"
        placeholder="Science Marks"
        onChange={handleChange}
      />

      <input
        type="number"
        name="english"
        placeholder="English Marks"
        onChange={handleChange}
      />

      <button onClick={handleSubmit}>
        Add Student
      </button>

    </div>
  );
}

export default App;