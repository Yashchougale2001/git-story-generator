import React from "react";

const getColor = (phase) => {
  if (phase.includes("Refactor")) return "#4caf50";
  if (phase.includes("Feature")) return "#ff9800";
  return "#f44336";
};

const Timeline = ({ phases }) => {
  return (
    <div>
      <h2>Project Story Timeline</h2>
      {phases.map((p, i) => (
        <div
          key={i}
          style={{
            background: getColor(p),
            color: "white",
            padding: "10px",
            margin: "8px 0",
            borderRadius: "6px"
          }}
        >
          {i + 1}. {p}
        </div>
      ))}
    </div>
  );
};

export default Timeline;
