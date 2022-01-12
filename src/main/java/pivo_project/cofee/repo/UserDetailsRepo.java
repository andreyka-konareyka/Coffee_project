package pivo_project.cofee.repo;

import org.springframework.data.jpa.repository.JpaRepository;
import pivo_project.cofee.domain.User;

public interface UserDetailsRepo extends JpaRepository<User, String> {
}
