import { Routes, Route } from "react-router-dom";
import UserForm from "./UserForm";
import ParkingSlotPage from "./parkingslotpage";

export default function App() {
  return (
    <Routes>
      <Route path="/" element={<UserForm />} />
      <Route path="/slot" element={<ParkingSlotPage />} />
    </Routes>
  );
}
