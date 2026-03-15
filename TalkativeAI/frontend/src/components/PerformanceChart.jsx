import {
  Chart as ChartJS,
  LineElement,
  CategoryScale,
  LinearScale,
  PointElement
} from "chart.js";

import { Line } from "react-chartjs-2";

ChartJS.register(
  LineElement,
  CategoryScale,
  LinearScale,
  PointElement
);

export default function PerformanceChart() {

  const data = {
    labels: ["Session1","Session2","Session3"],
    datasets: [
      {
        label: "Overall Score",
        data: [0.6,0.7,0.82]
      }
    ]
  };

  return <Line data={data} />;
}
