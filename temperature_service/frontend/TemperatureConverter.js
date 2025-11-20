import { useState } from "react";

export default function TemperatureConverter() {
  const [valor, setValor] = useState("");
  const [resultado, setResultado] = useState("");

  const convertC2F = async () => {
    if (valor === "") return;

    const res = await fetch(`/convert/c2f?c=${valor}`);
    const data = await res.json();
    setResultado(`${data.celsius}°C equivalen a ${data.fahrenheit}°F`);
  };

  const convertF2C = async () => {
    if (valor === "") return;

    const res = await fetch(`/convert/f2c?f=${valor}`);
    const data = await res.json();
    setResultado(`${data.fahrenheit}°F equivalen a ${data.celsius}°C`);
  };

  const limpiar = () => {
    setValor("");
    setResultado("");
  };

  return (
    <div style={{ padding: "20px", width: "300px", background: "#f5f5f5" }}>
      <h2>Conversión de Temperaturas</h2>

      <input
        type="number"
        value={valor}
        onChange={(e) => setValor(e.target.value)}
        placeholder="Ingrese valor"
        style={{ width: "100%", marginBottom: "10px", padding: "8px" }}
      />

      <button onClick={convertC2F}>Celsius → Fahrenheit</button>
      <button onClick={convertF2C}>Fahrenheit → Celsius</button>
      <button onClick={limpiar}>Limpiar</button>

      <div style={{ marginTop: "15px", fontWeight: "bold" }}>
        {resultado}
      </div>
    </div>
  );
}
