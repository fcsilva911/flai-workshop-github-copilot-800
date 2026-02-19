import React, { useState, useEffect } from 'react';

function Users() {
  const [users, setUsers] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  const apiUrl = `https://${process.env.REACT_APP_CODESPACE_NAME}-8000.app.github.dev/api/users/`;

  useEffect(() => {
    console.log('Users: fetching from', apiUrl);
    fetch(apiUrl)
      .then((response) => {
        if (!response.ok) {
          throw new Error(`HTTP error! status: ${response.status}`);
        }
        return response.json();
      })
      .then((data) => {
        console.log('Users: fetched data', data);
        // Support both paginated (.results) and plain array responses
        const items = Array.isArray(data) ? data : data.results || [];
        setUsers(items);
        setLoading(false);
      })
      .catch((err) => {
        console.error('Users: fetch error', err);
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

  return (
    <div className="card octofit-card mt-4">
      <div className="card-header bg-dark text-white">
        <h2 className="h4 mb-0">Users</h2>
      </div>
      <div className="card-body p-0">
        {users.length === 0 ? (
          <p className="text-muted p-3 mb-0">No users found.</p>
        ) : (
          <div className="table-responsive">
            <table className="table table-hover table-striped mb-0">
              <thead>
                <tr>
                  <th>Name</th>
                  <th>Email</th>
                  <th>Team ID</th>
                  <th>Created At</th>
                </tr>
              </thead>
              <tbody>
                {users.map((user, index) => (
                  <tr key={user._id || index}>
                    <td><strong>{user.name}</strong></td>
                    <td><a href={`mailto:${user.email}`} className="link-primary">{user.email}</a></td>
                    <td>{user.team_id}</td>
                    <td>{user.created_at ? new Date(user.created_at).toLocaleDateString() : ''}</td>
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

export default Users;
