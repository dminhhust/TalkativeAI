export default function ScenarioSelector({ setScenario }) {

  return (
    <div>

      <h2>Select Practice Mode</h2>

      <button
        onClick={() =>
          setScenario("job_interview")
        }
      >
        Job Interview
      </button>

      <button
        onClick={() =>
          setScenario("speaking_practice")
        }
      >
        Speaking Practice
      </button>

      <button
        onClick={() =>
          setScenario("random_topic")
        }
      >
        Random Topic
      </button>

    </div>
  );
}
