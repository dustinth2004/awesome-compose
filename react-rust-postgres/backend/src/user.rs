use tokio_postgres::{Error, GenericClient, Row};

/// Represents a user in the database.
#[derive(Debug, serde::Serialize)]
pub struct User {
    /// The user's ID.
    pub id: i32,
    /// The user's login name.
    pub login: String,
}

impl From<Row> for User {
    fn from(row: Row) -> Self {
        Self {
            id: row.get(0),
            login: row.get(1),
        }
    }
}

impl User {
    /// Returns all users from the database.
    pub async fn all<C: GenericClient>(client: &C) -> Result<Vec<User>, Error> {
        let stmt = client.prepare("SELECT id, login FROM users").await?;
        let rows = client.query(&stmt, &[]).await?;

        Ok(rows.into_iter().map(User::from).collect())
    }
}
