import React, { useState } from "react";

function MedTime({ mt, userInfo }) {
  //handle employee signing off time slot
  const [signedOff, setSignrdOff] = useState(mt.signed_off);
  const [color, setColor] = useState("");
  function onHandleSignOff() {
    console.log(userInfo);
    setSignrdOff((signedOff) => (signedOff = userInfo.name));
    console.log(mt.id);
    fetch(`/medication_times/${mt.id}`, {
      method: "PATCH",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({
        signed_off: userInfo.name,
      }),
    }).then((res) => {
      if (res.status === 204) setColor((color) => (color = "green"));
    });
  }

  return (
    <>
      <tbody>
        <tr className="text-start">
          <td>{mt.time_slot}</td>
          <td>
            <button
              style={{ backgroundColor: color }}
              onClick={onHandleSignOff}
            >
              {signedOff}
            </button>
          </td>
          <td>
            {mt.client_id}. {mt.clients.name}
          </td>
          <td>
            {mt.medication_id}. {mt.medications.name}
          </td>
        </tr>
      </tbody>
    </>
  );
}

export default MedTime;
