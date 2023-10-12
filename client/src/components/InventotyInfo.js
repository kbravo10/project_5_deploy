import React, { useState } from "react";

function InventoryInfo({ inv }) {
  const [invCount, setInvCount] = useState(inv.count_inventory);
  function onHandleAlter(e) {
    e.preventDefault();
    var action = "";
    if (e.target.value === "decrease") {
      action = "decrease";
    } else {
      action = "restock";
    }

    fetch(`/inventory/${inv.id}`, {
      method: "PATCH",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({
        action: action,
      }),
    }).then((r) => {
      if (r.status === 204) {
        if (action === "decrease") {
          setInvCount((invCount) => invCount - 1);
        } else {
          setInvCount((invCount) => (invCount = 10));
        }
      }
    });
  }
  return (
    <tbody>
      <tr class="text-start">
        <td>{inv.inventory}</td>
        <td>
          {invCount}
          <button onClick={onHandleAlter} value="decrease">
            decrease by 1
          </button>
          <button onClick={onHandleAlter} value="restock">
            Restock
          </button>
        </td>
        <td>{inv.instructions}</td>
      </tr>
    </tbody>
  );
}

export default InventoryInfo;
