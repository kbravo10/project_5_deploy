import React from "react";

function MedInfo({ med }) {
  return (
    <tbody>
      <tr class="text-start">
        <td>{med.name}</td>
        <td>{med.medication_use}</td>
      </tr>
    </tbody>
  );
}

export default MedInfo;
