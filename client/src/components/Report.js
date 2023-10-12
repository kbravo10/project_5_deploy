import React, { useEffect, useState } from "react";
import * as yup from "yup";
import { useFormik } from "formik";
import { Link } from "react-router-dom/cjs/react-router-dom.min";

function Report() {
  // usestate to get the fetch
  const [reports, setReports] = useState([]);
  const [refresh, setRefresh] = useState(false);
  const [visible, setVisible] = useState(false);
  const [clientName, setClientName] = useState([]);

  //fetch statem,ent to get data from report from backend
  useEffect(() => {
    fetch("/reports")
      .then((r) => r.json())
      .then((data) => {
        setReports(data.report);
        setClientName(data.client_name);
      });
  }, [refresh]);

  //declare requirements for report form
  const formSchema = yup.object().shape({
    type_of_report: yup.string().min(1).required("cannot be blank"),
    context: yup
      .string()
      .min(25)
      .required("Must be at least 25 characters long."),
    client_name: yup.string().required("cannot be blank"),
  });

  //handle making reports with the correct inputs
  const formik = useFormik({
    initialValues: {
      type_of_report: "",
      context: "",
      client_name: "",
    },
    validationSchema: formSchema,
    onSubmit: (values) => {
      fetch("reports", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify(values, null, 2),
      }).then((r) => {
        if (r.status === 201) {
          setRefresh(!refresh);
        }
      });
    },
  });
  return (
    <div>
      <h1>REPORTS</h1>
      <button onClick={() => setVisible(true)}>View reports</button>
      {visible
        ? reports.map((report, index) => {
            return (
              <div key={index}>
                <Link className="link" to={`/reports/${report.id}`}>
                  {report.type_of_report} -- {report.client_name} --{" "}

                </Link>
              </div>
            );
          })
        : null}
      <br></br>
      <div className="reportDiv">
        <h2>Make report</h2>
        <form className="reportForm" onSubmit={formik.handleSubmit}>
          <div className="reportTypeDiv">
            <label htmlFor="type_of_report">Type of Report</label>
            <br></br>
            <select
              id="type_of_report"
              name="type_of_report"
              onChange={formik.handleChange}
            >
              <option value={null}></option>
              <option value="small injury">Small Injury</option>
              <option value="Emergency">Emergency</option>
              <option value="End of shift">End of Shift</option>
            </select>
          </div>
          <p style={{ color: "red" }}> {formik.errors.type_of_report}</p>
          <div className="clientReport">
            <label htmlFor="client_id">Client involved</label>
            <select
              id="client_name"
              name="client_name"
              onChange={formik.handleChange}
            >
              <option value={null}></option>
              {clientName.map((name, index) => {
                return (
                  <option key={index} value={name}>
                    {name}
                  </option>
                );
              })}
            </select>
          </div>
          <p style={{ color: "red" }}> {formik.errors.client_name}</p>
          <div className="contextDiv">
            <label htmlFor="context">Report Summary</label>
            <br></br>
            <textarea
              style={{ width: "60vw", height: "10vw", text: "left" }}
              type="text"
              id="context"
              name="context"
              onChange={formik.handleChange}
              value={formik.values.context}
            />
          </div>
          <p style={{ color: "red" }}> {formik.errors.context}</p>
          <button type="submit">Submit Report</button>
        </form>
      </div>
    </div>
  );
}

export default Report;
