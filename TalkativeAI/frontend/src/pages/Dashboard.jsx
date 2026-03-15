import { useState } from "react";
import ScenarioSelector from "../components/ScenarioSelector";
import PracticePage from "./PracticePage";

export default function Dashboard({ token }) {

  const [scenario, setScenario] = useState(null);

  if (!scenario) {
    return (
      <ScenarioSelector
        setScenario={setScenario}
      />
    );
  }

  return (
    <PracticePage
      scenario={scenario}
      token={token}
    />
  );
}
