import axios from "axios";

const CommitInput = ({ onResult }) => {
  const analyzeCommits = async () => {
    const res = await axios.get("http://localhost:5000/analyze");
    onResult(res.data.phases);
  };

  return (
    <div>
      <button onClick={analyzeCommits}>
        Analyze Example Git History
      </button>
    </div>
  );
};

export default CommitInput;
