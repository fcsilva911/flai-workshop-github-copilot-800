import React, { useState, useEffect } from 'react';

function Leaderboard() {
  const [entries, setEntries] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  const apiUrl = `https://${process.env.REACT_APP_CODESPACE_NAME}-8000.app.github.dev/api/leaderboard/`;

  useEffect(() => {
    console.log('Leaderboard: fetching from', apiUrl);
    fetch(apiUrl)
      .then((response) => {
        if (!response.ok) {
          throw new Error(`HTTP error! status: ${response.status}`);
        }
        return response.json();
      })
      .then((data) => {
        console.log('Leaderboard: fetched data', data);
        // Support both paginated (.results) and plain array responses
        const items = Array.isArray(data) ? data : data.results || [];
        setEntries(items);
        setLoading(false);
      })
      .catch((err) => {
        console.error('Leaderboard: fetch error', err);
        setError(err.message);
        setLoading(false);
      });
  }, [apiUrl]);

  if (loading) return (
    <div className="octofit-spinner-wrapper">
      <div className="spinner-border text-primary" role="status">
        <span className="visually-hidden">Loading...</span>
      </div>
    </div>
  );

  if (error) return (
    <div className="alert alert-danger mt-4" role="alert">
      <strong>Error:</strong> {error}
    </div>
  );

  const rankBadgeClass = (rank) => {
    if (rank === 1) return 'badge rank-1';
    if (rank === 2) return 'badge rank-2';
    if (rank === 3) return 'badge rank-3';
    return 'badge bg-secondary';
  };

  return (
    <div className="card octofit-card mt-4">
      <div className="card-header bg-dark text-white">
        <h2 className="h4 mb-0">Leaderboard</h2>
      </div>
      <div className="card-body p-0">
        {entries.length === 0 ? (
          <p className="text-muted p-3 mb-0">No leaderboard entries found.</p>
        ) : (
          <div className="table-responsive">
            <table className="table table-hover mb-0">
              <thead>
                <tr>
                  <th>Rank</th>
                  <th>User ID</th>
                  <th>Total Calories</th>
                  <th>Total Activities</th>
                </tr>
              </thead>
              <tbody>
                {entries.map((entry, index) => (
                  <tr key={entry._id || index}>
                    <td><span className={rankBadgeClass(entry.rank)}>{entry.rank}</span></td>
                    <td>{entry.user_id}</td>
                    <td>{entry.total_calories}</td>
                    <td>{entry.total_activities}</td>
                  </tr>
                ))}
              </tbody>
            </table>
          </div>
        )}
      </div>
    </div>
  );
}

export default Leaderboard;
